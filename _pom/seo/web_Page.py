import requests
from bs4 import BeautifulSoup


class WebPage:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.html_content = None
        self.src_attributes = []

    def send_request(self):
        self.response = requests.get(self.url)

    def get_html_content(self):
        if self.response and self.response.status_code == 200:
            self.html_content = self.response.text

    def parse_src_attributes(self):
        if self.html_content:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            self.src_attributes = [tag.get("src") for tag in soup.find_all(attrs={"src": True})]

    def validate_src_links(self):
        failing_links = []
        results = []

        for src in self.src_attributes:
            full_url = src if src.startswith("http") else self.url + src
            try:
                response = requests.get(full_url)
                status = response.status_code
                results.append({"URL": full_url, "Status": status})

                if status == 200:
                    print(f"Validado: {full_url}")
                else:
                    failing_links.append(full_url)
                    print(f"Enlace no válido: {full_url}")
            except requests.exceptions.RequestException:
                failing_links.append(full_url)
                results.append({"URL": full_url, "Status": "Error"})

        # Lógica para escribir resultados en un archivo CSV
        self.write_results_to_csv(results)

        return failing_links

    def write_results_to_csv(self, results):
        csv_filename = "validation_results.csv"

        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["URL", "Status"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(results)

# Ejemplo de uso:
# webpage = WebPage("https://example.com")
# webpage.send_request()
# webpage.get_html_content()
# webpage.parse_src_attributes()
# failing_links = webpage.validate_src_links()
