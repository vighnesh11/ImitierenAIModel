import os
import openai
import config
import random
# Connect to Gpt-3 services
openai.api_key = config.OPENAI_API_KEY

# Type of phishing email
print("Type of phishing email\n1. Attachment\n2. Link")
phishing_type = input("Choice: ")
phishing_type = int(phishing_type)

while phishing_type > 2:
    print("Invalid input")
    print("Type of phishing email\n1. Attachment\n2. Link")
    phishing_type = input("Choice: ")
    phishing_type = int(phishing_type)

if phishing_type == 1:
    openAIPrompt = "Generate a cold email for the following proposal: {}"
    print("Attachment")
elif phishing_type == 2:
    openAIPrompt = "Generate a cold email for the following product: {}"
    print("Link")

# Email variables
target = input("Target's name: ")
masquerader = input("Masquerade as: ")
# print(openAIPrompt)

# Deep learning function to generate phishing email
def openAIQuery(query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=openAIPrompt.format(query),
        temperature=0.5,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)

    # Deep learning result validation
    if "choices" in response:
        if len(response["choices"]) > 0:
            answer = response["choices"][0]["text"]
        else:
            answer = "Opps sorry, email cannot be generated"
    else:
        answer = "Opps sorry, email cannot be generated"

    # Fine tune Email sender & receiver
    find_it1 = "____"
    find_it2 = "[Your name]"
    find_it3 = "[Your Name]"
    find_it4 = "Sir/Madam"
    repl_it1 = target
    repl_it2 = masquerader
    answer = answer.replace(find_it1, repl_it1)
    answer = answer.replace(find_it2, repl_it2)
    answer = answer.replace(find_it3, repl_it2)
    answer = answer.replace(find_it4, repl_it2)

    # Fine tune Email for phishing attachment
    if phishing_type == 1:
        r = random.choice(os.listdir("PhishingAttachments"))
        answer = answer + "\n\n" + "Attachment: " + r
        print(answer)
        # Save generated email to .txt file
        file = open("here.txt", "w")
        file.write(answer)
        file.close

    # Fine tune Email for phishing link
    if phishing_type == 2:
        s = open("phishinglinks.txt", "r")
        m = s.readlines()
        l = []
        for i in range(0, len(m) - 1):
            x = m[i]
            z = len(x)
            a = x[:z - 1]
            l.append(a)
        l.append(m[i + 1])
        o = random.choice(l)
        s.close()
        answer = answer + "\n\n" + "Click here now: " + o
        print(answer)
        # Save generated email to .txt file
        file = open("here.txt", "w")
        file.write(answer)
        file.close


# Input phishing content
query = input("Phishing content: ")
openAIQuery(query)

