#!/usr/bin/env python3

def exporter_vulnerabilites(vulns, package, version):
    # Exporter les vulnérabilités dans un fichier JSON
    filename = f"{package}_{version}_vulnerabilites.json"
    with open(filename, 'w') as f:
        json.dump(vulns, f, indent=4)
    print(f"Les résultats ont été exportés dans {filename}")

def rechercher_vulnerabilites(package, version, gravite=""):
    url = f"https://services.nvd.nist.gov/rest/json/cve/1.0/?keyword={package}&version={version}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if "result" in data and "CVE_Items" in data["result"]:
            vulns = data["result"]["CVE_Items"]
            results = []  # Liste pour stocker les résultats
            if vulns:
                print(f"Vulnérabilités trouvées pour {package} version {version} :\n")
                for vuln in vulns:
                    cve_id = vuln["cve"]["CVE_data_meta"]["ID"]
                    description = vuln["cve"]["description"]["description_data"][0]["value"]
                    
                    # Vérifier la gravité
                    cvss_score = vuln.get("impact", {}).get("baseMetricV2", {}).get("score", None)
                    if cvss_score:
                        # Filtrer par gravité
                        if gravite and float(cvss_score) < gravite:
                            continue
                        
                    vuln_data = {
                        "CVE_ID": cve_id,
                        "Description": description,
                        "CVSS_Score": cvss_score if cvss_score else "Non défini"
                    }
                    results.append(vuln_data)
                    print(f"CVE ID: {cve_id}")
                    print(f"Description: {description}")
                    print(f"CVSS Score: {cvss_score if cvss_score else 'Non défini'}")
                    print("-" * 80)
                
                # Exporter les résultats dans un fichier JSON
                exporter_vulnerabilites(results, package, version)
            else:
                print(f"Aucune vulnérabilité trouvée pour {package} version {version}.")
        else:
            print("Aucun résultat trouvé dans la base de données.")
    else:
        print(f"Erreur lors de la requête à l'API (code {response.status_code})")

if __name__ == "__main__":
    package = input("Entrez le nom du package: ")
    version = input("Entrez la version du package: ")
    gravite = input("Filtrer par gravité (score CVSS supérieur à): ")
    
    gravite = float(gravite) if gravite else None
    
    # Recherche des vulnérabilités
    rechercher_vulnerabilites(package, version, gravite)
