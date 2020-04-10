import csv
import os

base_folder = "C:/Users/Aaron Jacobson/Documents/UWB/19-20/Spring 20/BIS 498/pamhplets_text/2016"
topLineToPrint = ["race", "district", "name", "party", "has_opponent", "elected_experience",
                  "other_professional_experience",
                  "education", "community_service", "statement", "contact"]
candidateList = []
with open("2016_statements.tsv", 'w', newline='\n', encoding="utf8") as outputCsv:
    outputWriter = csv.writer(outputCsv, delimiter="\t", quotechar="~")
    outputWriter.writerow(topLineToPrint)

    for entry in os.listdir(base_folder):
        print("------------------------------Working on " + entry)
        numLines = 0
        with open(base_folder + "/" + entry, "r", encoding="utf8") as inputFile:
            numLines = len(list(inputFile))

        with open(base_folder + "/" + entry, "r", encoding="utf8") as inputFile:
            currentLine = 0
            line = inputFile.readline()
            currentLine += 1
            while currentLine < numLines:
                # print("On " + str(currentLine) + "/" + str(numLines))

                if line.count("|") > 1 and ("State Representative" in line or "State Senator" in line):
                    print("-" + line)
                    # the start of a new race section
                    firstCandidateToPrint = []
                    secondCandidateToPrint = []
                    words = str.split(line, " ")
                    indexOffset = 0
                    if str.isdigit(words[0]):
                        indexOffset = 1
                    race = words[0 + indexOffset] + " " + words[1 + indexOffset]
                    if words[1 + indexOffset] == "Representative":
                        race = race + " " + words[5 + indexOffset] + " " + words[6 + indexOffset]
                    district = words[4 + indexOffset]
                    firstCandidateToPrint.append(race.replace("\n", ""))
                    firstCandidateToPrint.append(district.replace("\n", ""))
                    secondCandidateToPrint.append(race.replace("\n", ""))
                    secondCandidateToPrint.append(district.replace("\n", ""))

                    # now we deal with the candidates individually
                    name_1 = inputFile.readline() + " " + inputFile.readline()
                    currentLine += 1
                    currentLine += 1
                    party_1 = inputFile.readline()
                    currentLine += 1
                    firstCandidateToPrint.append(name_1.replace("\n", ""))
                    firstCandidateToPrint.append(party_1.replace("\n", ""))
                    name_2 = inputFile.readline()
                    currentLine += 1
                    if "Unopposed" in name_2:
                        # no other candidate
                        firstCandidateToPrint.append("no_opponent".replace("\n", ""))
                        pass
                    else:
                        name_2 = name_2 + " " + inputFile.readline()
                        currentLine += 1
                        party_2 = inputFile.readline()
                        currentLine += 1
                        secondCandidateToPrint.append(name_2.replace("\n", ""))
                        secondCandidateToPrint.append(party_2.replace("\n", ""))
                        firstCandidateToPrint.append("has_opponent".replace("\n", ""))
                        secondCandidateToPrint.append("has_opponent".replace("\n", ""))

                    inputFile.readline()  # get rid of "Elected Experience" line
                    currentLine += 1

                    line = inputFile.readline()  # move onto the first line after "Elected Experience"
                    currentLine += 1
                    elected_experience_1 = ""
                    while line and "Other Professional Experience" not in line:
                        elected_experience_1 = elected_experience_1 + " " + line
                        line = inputFile.readline()
                        currentLine += 1
                    firstCandidateToPrint.append(elected_experience_1.replace("\n", ""))

                    line = inputFile.readline()  # move onto the first line after "Other Professional Experience"
                    currentLine += 1
                    other_professional_experience_1 = ""
                    while line and "Education" not in line:
                        other_professional_experience_1 = other_professional_experience_1 + " " + line
                        line = inputFile.readline()
                        currentLine += 1
                    firstCandidateToPrint.append(other_professional_experience_1.replace("\n", ""))

                    line = inputFile.readline()  # move onto first line after "Education"
                    currentLine += 1
                    education_1 = ""
                    while line and "Community Service" not in line:
                        education_1 = education_1 + " " + line
                        line = inputFile.readline()
                        currentLine += 1
                    firstCandidateToPrint.append(education_1.replace("\n", ""))

                    line = inputFile.readline()  # move onto the first line after "Community Service"
                    currentLine += 1
                    community_service_1 = ""
                    while line and "Statement" not in line:
                        community_service_1 = community_service_1 + " " + line
                        line = inputFile.readline()
                        currentLine += 1
                    firstCandidateToPrint.append(community_service_1.replace("\n", ""))

                    line = inputFile.readline()  # move onto the first line after "Statement"
                    currentLine += 1
                    statement_1 = ""
                    while line and "Contact" not in line:
                        statement_1 = statement_1 + " " + line
                        line = inputFile.readline()
                        currentLine += 1
                    firstCandidateToPrint.append(statement_1.replace("\n", ""))

                    if "Unopposed" in name_2:
                        line = inputFile.readline()  # move onto the first line after "Contact"
                        currentLine += 1
                        contact_1 = ""
                        while line and "|" not in line:
                            contact_1 = contact_1 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        firstCandidateToPrint.append(contact_1.replace("\n", ""))
                    else:
                        line = inputFile.readline()  # move onto the first line after "Contact"
                        currentLine += 1
                        contact_1 = ""
                        while line and "Elected Experience" not in line:
                            contact_1 = contact_1 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        firstCandidateToPrint.append(contact_1.replace("\n", ""))

                        # now onto the second candidate
                        line = inputFile.readline()  # move onto the first line after "Elected Experience"
                        currentLine += 1
                        elected_experience_2 = ""
                        while line and "Other Professional Experience" not in line:
                            elected_experience_2 = elected_experience_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(elected_experience_2.replace("\n", ""))

                        line = inputFile.readline()  # move onto the first line after "Other Professional Experience"
                        currentLine += 1
                        other_professional_experience_2 = ""
                        while line and "Education" not in line:
                            other_professional_experience_2 = other_professional_experience_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(other_professional_experience_2.replace("\n", ""))

                        line = inputFile.readline()  # move onto the first line after "Education"
                        currentLine += 1
                        education_2 = ""
                        while line and "Community Service" not in line:
                            education_2 = education_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(education_2.replace("\n", ""))

                        line = inputFile.readline()  # move onto the first line after "Community Service"
                        currentLine += 1
                        community_service_2 = ""
                        while line and "Statement" not in line:
                            community_service_2 = community_service_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(community_service_2.replace("\n", ""))

                        line = inputFile.readline()  # move onto the first line after "Statement"
                        currentLine += 1
                        statement_2 = ""
                        while line and "Contact" not in line:
                            statement_2 = statement_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(statement_2.replace("\n", ""))

                        line = inputFile.readline()  # move onto the first lane after "Contact"
                        currentLine += 1
                        contact_2 = ""
                        while line and "|" not in line:
                            contact_2 = contact_2 + " " + line
                            line = inputFile.readline()
                            currentLine += 1
                        secondCandidateToPrint.append(contact_2.replace("\n", ""))
                    # write both candidates
                    if name_1 not in candidateList:
                        print("--------------------------------Found " + name_1 + " for " + race + " in " + district)
                        candidateList.append(name_1.replace("\n", ""))
                        outputWriter.writerow(firstCandidateToPrint)
                    if name_2 not in candidateList and "Unopposed" not in name_2:
                        print("--------------------------------Found " + name_2 + " for " + race + " in " + district)
                        candidateList.append(name_2.replace("\n", ""))
                        outputWriter.writerow(secondCandidateToPrint)

                else:
                    line = inputFile.readline()
                    currentLine += 1

        pass

    pass
