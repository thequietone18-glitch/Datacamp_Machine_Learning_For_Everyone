# What does your data look like? (II)
# In the previous exercise you looked at the distribution of individual columns. While this is a good start, a more detailed view of how different features interact with each other may be useful as this can impact your decision on what to transform and how.

# Instructions 1/2
# 50 XP
# Import matplotlib's pyplot module as plt.
# Import seaborn as sns.
# Plot pairwise relationships in the so_numeric_df dataset.
# Show the plot.

# Instructions 2/2
# 50 XP
# Print the summary statistics of the so_numeric_df DataFrame.


# # Import packages (Instruction 1)
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Plot pairwise relationships
# sns.pairplot(so_numeric_df)

# # Show plot
# plt.show()


# Print summary statistics (Instruction 2)
print(so_numeric_df.describe())
