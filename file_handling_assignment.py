# Open a new file
with open('my_file.txt', 'w') as file:
    # Writing lines of text
    file.write("Our vision is to empower Africa's youth through software development \n")
    file.write("The 16-week software development training will empower you with the skills to launch your tech career. \n")
    file.write("WhatsApp: +254 700 611 875 \n")

print("File created and written successfully.")

# Open the file in append mode
with open('my_file.txt', 'a') as file:
    # Append three additional lines
    file.write("Our Mission to train one million developers for Africa with quality, affordable and accessible training supporting youths by providing world-class tech training to grow their tech skills and set them apart. \n")
    file.write("The program offers a fully-funded, virtual and self-paced software development training program that covers four technical modules alongside entrepreneurship and personal development. \n")
    file.write("Learning is delivered entirely online, allowing you to learn anytime, anywhere, and at your own pace with a vibrant community by your side. \n")

print("File appended successfully.")

# Open the file in read mode
with open('my_file.txt', 'r') as file:
    # Read and display each line
    for line in file:
        print(line.strip())   #Strip removes the newline character at the end of each line

print("File read and displayed successfully.")

try:
    # Open the file in append mode
    with open('my_file.txt', 'a') as file:
        # Append three additional lines
        file.write("The demand for digital skills has drastically increased, leaving individuals and businesses.\n")
        file.write("without adequate training struggling to keep up with the pace of change.\n")
        file.write("leading to an irreversible shift from traditional ways of doing things.\n")

except FileNotFoundError:
    print("File not found error occured.")
except PermissionError:
    print("Permission denied error occured.")
except Exception as e:
    print(f"An error occured: {e}")
else:
    print("File appended successfully.")
finally:
    try:
        # Open the file in read mode
        with open('my_file.txt', 'r') as file:
            # Read and display each line
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found error occurred.")
    except PermissionError:
        print("Permission denied error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("File read and displayed after append.")


