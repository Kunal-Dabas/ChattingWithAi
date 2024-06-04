import google.generativeai as genai
import os
import zipfile

API_KEY = "AIzaSyDzjdE8b_F_DTnGol6XOijmdqY9Q4HZaAE"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


def chat_ai( prompt ):
    response = model.generate_content(prompt)
    return response.text

zip_path = 'example.zip'
def create_file_in_zip(zip_path, files_with_content):
    with zipfile.ZipFile(zip_path, 'a') as zip_ref:
        for file_name, content in files_with_content.items():
            # Create a new file within the ZIP archive
            zip_ref.writestr(file_name, content)
            print(f"Added {file_name} to {zip_path}")

def create_file( data , num ):
    files_with_content = {
    f'{num}.txt': f'{data}'
    }
    create_file_in_zip(zip_path, files_with_content)
    # filename = f"{num}.txt"
    # with open(filename, "w") as file:
    #     file.write(data)

if __name__ == "__main__":
    num = 20
    while (num > 0):
        user_input = input("You : ")
        if user_input.lower() in ["quit" , "exit"]:
            break
        response = chat_ai(user_input)
        create_file( response , num )
        num = num-1