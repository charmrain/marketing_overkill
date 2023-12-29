import pandas as pd

# Assuming 'C:\Users\User\Desktop\data.txt' contains your company information
with open(r'C:\Users\User\Desktop\data.txt', 'r') as file:
    lines = file.readlines()

# Initialize variables
company_blocks = []
current_block = []

# Process each line of the file
for line in lines:
    line = line.strip()

    # If the line is not empty, add it to the current block
    if line:
        current_block.append(line)
    else:
        # Check if the current block has 10 lines (based on the presence of "Website:")
        if current_block and "Website:" in current_block[4]:
            # If the current block has 10 lines, add it to the list of company blocks
            company_blocks.append(current_block)
        elif current_block:
            # If the current block has 9 lines, add a placeholder for the missing Website line
            current_block.insert(4, "Website: N/A")
            company_blocks.append(current_block)
        
        current_block = []

# Check and add the last block (if any) after processing all lines
if current_block:
    if len(current_block) == 9:
        current_block.insert(4, "Website: N/A")
    company_blocks.append(current_block)

# Create a DataFrame from the data
columns = ['Company Name', 'Street Address', 'City/State/Zip', 'Phone', 'Website', 'Employees', 'Receipts', 'Start Date', 'More Detail', 'link']
df = pd.DataFrame(company_blocks, columns=columns)

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)
