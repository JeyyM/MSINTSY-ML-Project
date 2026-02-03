import numpy as np
import pandas as pd

class Functions:
    def __init__(self):
        pass

    def view_duplicates(self, df):
        total_rows = len(df)
        
        duplicates = df.duplicated()
        duplicate_count = duplicates.sum()
        
        print(f"Duplicate Row Check:")
        print(f"Total rows: {total_rows}")
        print(f"Duplicate rows: {duplicate_count}")

    def print_unique(self, df, column_name):
        if column_name not in df.columns:
            print(f"Column '{column_name}' not found")
            return
        
        value_counts = df[column_name].value_counts(dropna=False)
        total_rows = len(df)
        
        print(f"All unique responses in '{column_name}':")
        
        for value, count in value_counts.items():
            percentage = (count / total_rows) * 100
            print(f"{value}: {count} ({percentage:.2f}%)")
        
        print(f"\nTotal unique responses: {len(value_counts)}")
        print(f"Data type: {df[column_name].dtype}")
        
    def compress_mainbranch(self, x):
        x = x.lower()

        if x == "i am a developer by profession":
            return "professional dev"

        elif x == "i am not primarily a developer, but i write code sometimes as part of my work/studies":
            return "non-primary dev"

        elif x in [
            "i am learning to code",
            "i code primarily as a hobby",
        ]:
            return "learner or hobbyist"

        elif x in [
            "i used to be a developer by profession, but no longer am",
            "i work with developers or my work supports developers but am not a developer by profession",
        ]:
            return "retired or non-dev"

        else:
            return "retired or non-dev"
        
    # Compress education levels and handle nan
    def compress_education(self, ed_level):
        if pd.isna(ed_level):
            return 'other'
        elif 'Bachelor' in str(ed_level):
            return 'bachelor'
        elif 'Master' in str(ed_level):
            return 'master'
        elif 'Some college' in str(ed_level):
            return 'went to college without degree'
        elif 'Secondary school' in str(ed_level):
            return 'secondary school'
        elif 'Professional degree' in str(ed_level):
            return 'professional'
        elif 'Associate degree' in str(ed_level):
            return 'associate'
        elif 'Primary' in str(ed_level):
            return 'primary school'
        else:
            return 'other'
    
    # Compress employment status and handle nan
    def compress_employment(self, employment):
        if pd.isna(employment):
            return 'others'
        elif 'Employed' in str(employment):
            return 'employed'
        elif 'Independent' in str(employment):
            return 'independent'
        elif 'Student' in str(employment):
            return 'student'
        elif 'Not employed' in str(employment):
            return 'unemployed'
        elif 'Retired' in str(employment):
            return 'retired'
        elif 'I prefer not to say' in str(employment):
            return 'others'
        else:
            return 'others'
    
    # Compress developer type and handle nan
    def compress_devtype(self, dev_type):
        if pd.isna(dev_type):
            return 'others'
        
        dev_type_str = str(dev_type).lower()
        
        if dev_type_str == 'developer, full-stack':
            return 'full-stack developer'
        
        elif dev_type_str == 'developer, back-end':
            return 'backend developer'
        
        elif dev_type_str == 'developer, front-end':
            return 'frontend developer'
        
        elif dev_type_str == 'developer, mobile':
            return 'mobile developer'
        
        elif dev_type_str == 'developer, desktop or enterprise applications':
            return 'desktop developer'
        
        elif dev_type_str == 'developer, embedded applications or devices':
            return 'embedded developer'
        
        elif dev_type_str == 'developer, game or graphics':
            return 'game developer'
        
        elif dev_type_str == 'developer, qa or test':
            return 'qa tester'
        
        elif dev_type_str in ['developer, ai apps or physical ai', 'ai/ml engineer']:
            return 'ai/ml developer'
        
        elif dev_type_str == 'architect, software or solutions':
            return 'software architect'
        
        elif dev_type_str in ['data engineer', 'data scientist', 'data or business analyst']:
            return 'data specialist'
        
        elif dev_type_str in ['devops engineer or professional', 'cloud infrastructure engineer', 'system administrator']:
            return 'devops/infrastructure'
        
        elif dev_type_str == 'database administrator or engineer':
            return 'database specialist'
        
        elif dev_type_str == 'cybersecurity or infosec professional':
            return 'security specialist'
        
        elif dev_type_str in ['engineering manager', 'product manager', 'project manager']:
            return 'manager'
        
        elif dev_type_str in ['senior executive (c-suite, vp, etc.)', 'founder, technology or otherwise']:
            return 'executive/leader'
        
        elif dev_type_str in ['academic researcher', 'applied scientist']:
            return 'researcher/scientist'
        
        elif dev_type_str in ['support engineer or analyst', 'financial analyst or engineer']:
            return 'support/analyst'
        
        elif dev_type_str == 'ux, research ops or ui design professional':
            return 'ux/ui designer'
        
        elif dev_type_str == 'student':
            return 'student'
        
        elif dev_type_str == 'retired':
            return 'retired'        
        else:
            return 'others'
            
    # Assign nominal value to orgsize
    def orgsize_ordinal(self, x):
        if pd.isna(x) or x == "I don't know":
            return 0

        mapping = {
            "Just me - I am a freelancer, sole proprietor, etc.": 1,
            "Less than 20 employees": 2,
            "20 to 99 employees": 2,
            "100 to 499 employees": 3,
            "500 to 999 employees": 4,
            "1,000 to 4,999 employees": 5,
            "5,000 to 9,999 employees": 6,
            "10,000 or more employees": 7,
        }

        return mapping.get(x, 0)