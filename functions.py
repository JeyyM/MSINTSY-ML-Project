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
            
    # Compress learncodeai answers and handle nan
    def compress_learncodeai(self, learncodeai):
        if pd.isna(learncodeai):
            return 'others'
        elif 'Yes' in str(learncodeai):
            return 'yes'
        elif 'No' in str(learncodeai):
            return 'no'
        else:
            return 'others'
        
    # Compress aiselect and handle nan
    def compress_aiselect(self, aiselect):
        if pd.isna(aiselect):
            return 'others'
        elif 'daily' in str(aiselect):
            return 'daily'
        elif 'weekly' in str(aiselect):
            return 'weekly'
        elif 'infrequently' in str(aiselect):
            return 'infrequently'
        elif 'No' in str(aiselect):
            return 'no'
        else:
            return 'others'
        
    # Compress aiagents and handle nan
    def compress_aiagents(self, aiagents):
        if pd.isna(aiagents):
            return 'others'
        elif 'daily' in str(aiagents):
            return 'daily'
        elif 'weekly' in str(aiagents):
            return 'weekly'
        elif 'monthly' in str(aiagents):
            return 'monthly'
        elif 'No' in str(aiagents):
            return 'no'
        else:
            return 'others'
        
    # Compress aiagentchange and handle nan
    def compress_aiagentchange(self, aiagentchange):
        if pd.isna(aiagentchange):
            return 'others'
        elif 'great' in str(aiagentchange):
            return 'yes_greatly'
        elif 'somewhat' in str(aiagentchange):
            return 'yes_somewhat'
        elif 'minimally' in str(aiagentchange):
            return 'yes_minimally'
        elif 'No' in str(aiagentchange):
            return 'no'
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
    
    def process_tool_count(self, value):
        if pd.isna(value):
            return 0
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0
    
    def group_tool_count(self, value):
        tool_count = self.process_tool_count(value)
        
        if tool_count == 0:
            return '0'
        elif 1 <= tool_count <= 5:
            return '1 to 5'
        elif 6 <= tool_count <= 10:
            return '6 to 10'
        elif 11 <= tool_count <= 15:
            return '11 to 15'
        elif 16 <= tool_count <= 20:
            return '16 to 20'
        else:  # More than 20
            return 'More than 20'
        
    def group_countries(self, country):
        # Follows the UN Geoscheme for regional grouping
        if pd.isna(country):
            return "other"

        country = str(country).strip()

        northern_america = [
            "United States of America", "Canada"
        ]

        western_europe = [
            "Germany", "France", "Netherlands", "Belgium", "Austria",
            "Switzerland", "Luxembourg", "United Kingdom of Great Britain and Northern Ireland",
            "Ireland"
        ]

        northern_europe = [
            "Sweden", "Norway", "Denmark", "Finland", "Iceland", "Estonia", "Latvia", "Lithuania"
        ]

        southern_europe = [
            "Spain", "Italy", "Portugal", "Greece", "Malta", "Cyprus", "Croatia", "Slovenia"
        ]

        eastern_europe = [
            "Poland", "Czech Republic", "Slovakia", "Hungary", "Romania", "Bulgaria",
            "Ukraine", "Belarus", "Moldova", "Republic of Moldova", "Serbia", "Bosnia and Herzegovina",
            "Montenegro", "North Macedonia", "Republic of North Macedonia", "Albania", "Kosovo",
            "Russian Federation"
        ]

        eastern_asia = [
            "China", "Japan", "South Korea", "Republic of Korea", "North Korea", 
            "Democratic People's Republic of Korea", "Mongolia", "Taiwan", "Hong Kong (S.A.R.)"
        ]

        south_eastern_asia = [
            "Philippines", "Indonesia", "Thailand", "Malaysia", "Vietnam", "Viet Nam",
            "Singapore", "Myanmar", "Cambodia", "Laos", "Lao People's Democratic Republic", 
            "Brunei", "Brunei Darussalam", "Timor-Leste"
        ]

        southern_asia = [
            "India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal", "Bhutan", "Maldives",
            "Afghanistan"
        ]

        western_asia = [
            "Turkey", "Israel", "Jordan", "Lebanon", "Saudi Arabia", "United Arab Emirates",
            "Qatar", "Kuwait", "Bahrain", "Oman", "Yemen", "Iraq", "Iran", "Iran, Islamic Republic of...", 
            "Syria", "Syrian Arab Republic", "Palestine", "Georgia", "Armenia", "Azerbaijan"
        ]

        central_asia = [
            "Kazakhstan", "Uzbekistan", "Turkmenistan", "Kyrgyzstan", "Tajikistan"
        ]

        northern_africa = [
            "Egypt", "Libya", "Libyan Arab Jamahiriya", "Tunisia", "Algeria", "Morocco", "Sudan"
        ]

        western_africa = [
            "Nigeria", "Ghana", "Senegal", "Ivory Coast", "Côte d'Ivoire", "Mali", "Burkina Faso",
            "Niger", "Guinea", "Guinea-Bissau", "Benin", "Togo", "Sierra Leone", "Liberia",
            "Mauritania", "Gambia", "Cape Verde"
        ]

        eastern_africa = [
            "Kenya", "Uganda", "Tanzania", "United Republic of Tanzania", "Ethiopia", "Rwanda", "Burundi", "Somalia",
            "Madagascar", "Mauritius", "Djibouti"
        ]

        middle_africa = [
            "Cameroon", "Central African Republic", "Chad", "Republic of the Congo",
            "Congo, Republic of the...", "Democratic Republic of the Congo", "Gabon", "Equatorial Guinea",
            "Angola"
        ]

        southern_africa = [
            "South Africa", "Botswana", "Namibia", "Zimbabwe", "Zambia", "Mozambique", "Malawi",
            "Swaziland", "Lesotho"
        ]
        
        central_america = [
            "Mexico", "Guatemala", "Honduras", "El Salvador", "Nicaragua", "Costa Rica", "Panama", "Belize"
        ]

        caribbean = [
            "Cuba", "Dominican Republic", "Jamaica", "Trinidad and Tobago", "Barbados", "Puerto Rico",
            "Haiti", "Saint Lucia", "Antigua and Barbuda", "Guyana", "Suriname"
        ]

        south_america = [
            "Brazil", "Argentina", "Chile", "Colombia", "Peru", "Venezuela",
            "Venezuela, Bolivarian Republic of...", "Ecuador", "Uruguay", "Paraguay", "Bolivia"
        ]

        australia_new_zealand = [
            "Australia", "New Zealand", "Fiji"
        ]

        if country in northern_america:
            return "northern_america"

        elif country in western_europe:
            return "western_europe"
        elif country in northern_europe:
            return "northern_europe"
        elif country in southern_europe:
            return "southern_europe"
        elif country in eastern_europe:
            return "eastern_europe"

        elif country in eastern_asia:
            return "eastern_asia"
        elif country in south_eastern_asia:
            return "south_eastern_asia"
        elif country in southern_asia:
            return "southern_asia"
        elif country in western_asia:
            return "western_asia"
        elif country in central_asia:
            return "central_asia"

        elif country in northern_africa:
            return "northern_africa"
        elif country in western_africa:
            return "western_africa"
        elif country in eastern_africa:
            return "eastern_africa"
        elif country in middle_africa:
            return "middle_africa"
        elif country in southern_africa:
            return "southern_africa"

        elif country in central_america:
            return "central_america"
        elif country in caribbean:
            return "caribbean"
        elif country in south_america:
            return "south_america"

        elif country in australia_new_zealand:
            return "australia_new_zealand"

        else:
            return "other"
    
    def print_other_countries(self, df):        
        unique_countries = df['Country'].dropna().unique()
        
        other_countries = []
        for country in unique_countries:
            if self.group_countries(country) == "other":
                other_countries.append(country)
        
        other_country_counts = df[df['Country'].isin(other_countries)]['Country'].value_counts()
                
        for country, count in other_country_counts.items():
            percentage = (count / len(df)) * 100
            print(f"{country}: {count} ({percentage:.2f}%)")
        
        total_other = other_country_counts.sum()
        total_percentage = (total_other / len(df)) * 100
        print(f"Total 'other': {total_other} ({total_percentage:.2f}%)")
        
        return other_countries

    def clean_special(self, text):   
        clean_text = str(text).lower()
        clean_text = clean_text.replace(' ', '_')
        clean_text = clean_text.replace('/', '_')
        clean_text = clean_text.replace('#', 'sharp')
        clean_text = clean_text.replace('+', 'plus')
        clean_text = clean_text.replace('.', '_')
        clean_text = clean_text.replace('-', '_')
        clean_text = clean_text.replace('(', '')
        clean_text = clean_text.replace(')', '')
        
        return clean_text

    def skill_setup(self, df, column_name, verbose=True):
        skill_sequence = df[column_name].dropna()
        
        all_skills = []
        for entry in skill_sequence:
            if pd.isna(entry):
                continue
            skills = [skill.strip() for skill in str(entry).split(';') if skill.strip()]
            all_skills.extend(skills)
        
        skill_counts = pd.Series(all_skills).value_counts()
        
        total_responses = len(skill_sequence)
        total_skills = len(all_skills)
        unique_skills = len(skill_counts)
        
        if verbose:
            print(f"Skill Analysis for '{column_name}':")
            # print(f"Total responses with data: {total_responses:,}")
            # print(f"Total individual skill selections: {total_skills:,}")
            print(f"Unique skills: {unique_skills}")
            print(f"Average skills count: {total_skills/total_responses:.2f}")
        
        # print("\nTop skills by frequency:")
        
        # for skill, count in skill_counts.items():
        #     percentage = (count / total_responses) * 100
        #     print(f"{skill}: {count:,} ({percentage:.1f}%)")
        
        return skill_counts

    def encode_skills(self, df, column_name, prefix, top_perc=25, verbose=True):
        skill_counts = self.skill_setup(df, column_name, verbose=verbose)
        
        # Calculate top N skills based on percentage
        total_unique_skills = len(skill_counts)
        top_n = max(1, round(total_unique_skills * (top_perc / 100)))
        
        # Get top N skills
        top_skills = skill_counts.head(top_n).index.tolist()
        
        if verbose:
            print(f"Using top {top_perc}% = {top_n} skills out of {total_unique_skills} total")
            print(f"Skills: {top_skills}")
        
        skill_features = pd.DataFrame(index=df.index)
        
        for skill in top_skills:
            clean_name = self.clean_special(skill)
            column_name_clean = f"{prefix}_{clean_name}"
            
            # Check if it got used
            skill_features[column_name_clean] = df[column_name].apply(
                lambda x: 1 if pd.notna(x) and skill in str(x).split(';') else 0
            )
        
        if verbose:
            print(f"\nSkill features created:")
            print(f"Shape: {skill_features.shape}")
            print(f"Columns: {list(skill_features.columns)}")
            
            print(f"\nTop {top_n} skill usage rates:")
            for col in skill_features.columns[:20]:
                usage_rate = skill_features[col].mean() * 100
                skill_name = col.replace(f'{prefix}_', '').replace('_', ' ')
                print(f"{skill_name}: {usage_rate:.1f}%")
        
        return skill_features

