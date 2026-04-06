import csv

input_file = "D:/CDAC/MySQL/AI_impact/newAI_Impact_on_Jobs_2030.csv"
output_file = "cleaned_jobs.csv"

clean_data = []
seen = set()

with open(input_file, "r") as file:
    reader = csv.reader(file)
    
    header = next(reader)  # skip header
    clean_data.append(header)

    for row in reader:

        # 1. Remove extra spaces
        row = [value.strip() for value in row]

        # 2. Skip empty rows
        if not row or row[0] == "":
            continue

        try:

            # 3. Fix Data Types
            job_title = row[0]
            avg_salary = float(row[1])
            experience = int(row[2])
            education = row[3]
            ai_index = float(row[4])
            tech_growth = float(row[5])
            automation_prob = float(row[6])
            risk = row[7].capitalize()

            # 4. Handle Missing Values
            if job_title == "":
                continue

            if education == "":
                education = "Unknown"

            # 5. Validate ENUM (Risk_Category)
            if risk not in ["Low", "Medium", "High"]:
                risk = "Medium"

            # 6. Filter Invalid Data
            if avg_salary <= 0:
                continue

            if experience < 0:
                continue

            if not (0 <= ai_index <= 1):
                continue

            if not (0 <= tech_growth <= 1):
                continue

            if not (0 <= automation_prob <= 1):
                continue

            # 7. Remove duplicates
            row_tuple = (
                job_title, avg_salary, experience,
                education, ai_index, tech_growth,
                automation_prob, risk
            )

            if row_tuple in seen:
                continue

            seen.add(row_tuple)

            # 8. Append cleaned row
            clean_data.append([
                job_title,
                avg_salary,
                experience,
                education,
                ai_index,
                tech_growth,
                automation_prob,
                risk
            ])

        except:
            # skip rows with errors
            continue

# 9. Save cleaned CSV
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(clean_data)

print(" Saved as cleaned_jobs.csv")