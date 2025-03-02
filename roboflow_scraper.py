from bs4 import BeautifulSoup

def scrape_filenames(file_path):
    try:
        # Read the local HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse the page content
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all span elements
        spans = soup.find_all('span')
        filenames = []
        
        for span in spans:
            if "Filename :" in span.get_text():
                # Get the next sibling text
                next_text = span.find_next_sibling(string=True)
                if next_text:
                    filenames.append(next_text.strip())
        
        return filenames
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # file_path = input("Enter the local HTML file path: ")
    file_path = "/Users/markfisher/Desktop/targetSite.html"
    filenames = scrape_filenames(file_path)
    
    if filenames:
        print("Extracted Filenames:")
        for filename in filenames:
            print(filename)
    else:
        print("No filenames found.")
