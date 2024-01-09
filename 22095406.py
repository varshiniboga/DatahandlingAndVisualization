#DataSourceLink : https://www.kaggle.com/datasets/sriharshaeedala/u-s-government-revenue-collections
#GithubLink :

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('USGovtRevCollect_20041001_20231227.csv')

# Set up the dashboard layout
fig , axes = plt.subplots(nrows=2 , ncols=2 , figsize=(16 , 12))
fig.suptitle('Government Revenue Collection Analysis Dashboard' ,
             fontsize=16 , fontweight='bold')

government_palette = ["#1f78b4" , "#33a02c" , "#e31a1c" , "#ff7f00"]

# Set background color for the entire dashboard
fig.set_facecolor('#f0f0f0')

# Analysis 1: Bar Plot - Net Collections Amount by Electronic Category
sns.barplot(x='Electronic Category Description' , y='Net Collections Amount' ,
            data=df , ax=axes[0 , 0] , palette=government_palette)
axes[0 , 0].set_title('Net Collections Amount by Electronic Category' , fontweight='bold')
axes[0 , 0].tick_params(axis='x' ,  rotation=60)

# Analysis 2: Line Plot - Net Collections Amount over Calendar Month Number
sns.lineplot(x='Calendar Month Number' , y='Net Collections Amount' , data=df ,
             ax=axes[0 , 1] , palette=government_palette)
axes[0 , 1].set_title('Net Collections Amount over Calendar Month' , fontweight='bold')
axes[0 , 1].tick_params(axis='x' , rotation=60)

# Analysis 3: Pie Plot - Distribution of Tax Categories
tax_category_counts = df['Tax Category Description'].value_counts()
axes[1 , 0].pie(tax_category_counts , labels=tax_category_counts.index ,
               autopct='%1.1f%%', startangle=90, colors=government_palette)
axes[1 , 0].set_title('Distribution of Tax Categories' , fontweight='bold')

# Analysis 4: Bar Plot - Net Collections Amount by Channel Type
sns.barplot(x='Channel Type Description' , y='Net Collections Amount' ,
            data=df , ax=axes[1 , 1] , palette=government_palette)
axes[1 , 1].set_title('Net Collections Amount by Channel Type' , fontweight='bold')
axes[1 , 1].tick_params(axis='x' , rotation=60)

# Add text annotations
text = "1. In the electronic category, 'Fully electronic -all'\n" \
       " has the largest net collections.\n" \
       "2. April has the highest Net collections. \n" \
       "3. At 46.6%, 'Non-tax' is the highest tax category out of all of them.\n" \
       "4. According to channel type, net collections are higher on the internet."
axes[0 , 1].text(1.1 , 0.5 , text , transform=axes[0 , 1].transAxes ,
                fontsize=12 , va='center' , ha='left')

text = "Student Name : Sreevarshini Boga\n" \
       "Student Id : 22095406"
axes[1 , 1].text(1.1 , 0.5 , text , transform=axes[1 , 1].transAxes ,
                fontsize=12 , va='center' , ha='left' , fontweight='bold')

# Adjust layout
plt.tight_layout(rect=[0 , 0 , 1 , 0.96])
plt.savefig('22095406.png',dpi=300)

# Show the dashboard
# plt.show()
