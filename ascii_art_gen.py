import pyfiglet

def list_fonts():  
    available_fonts = pyfiglet.FigletFont.getFonts()  
    return available_fonts  

def generate_ascii_art(text, font='standard'):  
    ascii_art = pyfiglet.figlet_format(text, font=font)  
    return ascii_art  

def display_all_fonts(text):   
    fonts = list_fonts()  
    for font in fonts:  
        ascii_art = pyfiglet.figlet_format(text, font=font)  
        print(f"\nFont: {font}\n{ascii_art}")  

if __name__ == "__main__":
    # ANSI escape codes for colors
    GREEN = "\033[92m"
    RED = "\033[31m"
    RESET = "\033[0m"  

    dev = f"""
{GREEN}
    BY      
         ███▄    █  ▄▄▄       ███▄ ▄███▓▒███████▒
         ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▒ ▒ ▒ ▄▀░
        ▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░░ ▒ ▄▀▒░ 
        ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██   ▄▀▒   ░
        ▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒▒███████▒
        ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░▒▒ ▓░▒░▒
        ░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░░░▒ ▒ ░ ▒
           ░   ░ ░   ░   ▒   ░      ░   ░ ░ ░ ░ ░
                 ░       ░  ░       ░     ░ ░    
                                        ░        

                                      
                                    
{RESET}
    """
    print("=" * 50)

    ascii_generator = pyfiglet.figlet_format("ASCII Art Generator")
    print(f"{RED}{ascii_generator}{RESET}")
    print(dev)
    

    while True:
        print("\nChoose an option:")
        print("1. Display all available fonts")
        print("2. Generate ASCII art for a given text")
        print("3. Display all ASCII art with the specified text")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Available Fonts:")  
            fonts = list_fonts()  
            for i, font in enumerate(fonts, start=1):  
                print(f"{i}. {font}") 

        elif choice == "2":
            fonts = list_fonts()   
            text = input("\nEnter text to convert to ASCII art: ")   
            while True:  
                font_choice = input("Enter font number (leave empty for 'standard'): ")  
                if font_choice.isdigit() and 1 <= int(font_choice) <= len(fonts):  
                    font = fonts[int(font_choice) - 1]   
                    break  
                elif font_choice.strip() == "":  
                    font = 'standard' 
                    break  
                else:  
                    print("Invalid choice. Please enter a valid font number or leave empty.") 
            ascii_art = generate_ascii_art(text, font)

            print("\nASCII Art:\n")  
            print(ascii_art)  

        elif choice == "3":
            text = input("\nEnter text to display ASCII art for: ")
            display_all_fonts(text)
        elif choice == "4":
            break
