# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in 'tips' dataset from seaborn
tips = sns.load_dataset('tips')

# Create a boxplot showing total bills for each day
sns.boxplot(x="day", y="total_bill", data=tips)

# Setting the title
plt.title('Boxplot of Total Bill by Day')

# Display the plot
plt.show()
