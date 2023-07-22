import PyPDF2
from gtts import gTTS


def extract_text_from_pdf(pdf_file):
    # defining empty string
    text = ""
    # opening pdf file in read binary mode
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        from_page = 8  # replace it with page number you want to start from
        num_pages = len(pdf_reader.pages)

        for page_num in range(from_page, num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def convert_text_to_audio(text, output_audio_file):
    # converting text to audio and saving audio file
    tts = gTTS(text, lang='en')  # 'en' stands for english , replace it to language of your pdf file
    tts.save(output_audio_file)


def main():
    pdf_file_path = '/your_file.pdf'  # replace ''/your_file.pdf'' with your file path
    audio_output_file = 'output_audio.mp3'  # replace 'output_audio.mp3' with desirable name

    # calling the functions and passing parameters
    text = extract_text_from_pdf(pdf_file_path)
    convert_text_to_audio(text, audio_output_file)
    # optional print statement just to make sure conversion is done
    print(f"PDF to audio conversion completed. Audio file saved as '{audio_output_file}'.")


main()
