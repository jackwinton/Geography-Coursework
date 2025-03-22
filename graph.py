mport matplotlib.pyplot as plt

# Estimated percentage time saved using the NSR compared to the Suez Canal during different months in 2024.
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
percent_saved = [15, 20, 25, 30, 35, 40, 45, 50, 50, 40, 30, 20]  # [1], [2], Estimated percentage saved from Suez Canal time

# Estimated additional cost per ton due to icebreaker use and transshipment ($ per ton)
# More ice means higher costs, so costs are higher in winter and lower in summer
icebreaker_cost_per_ton = [50, 45, 40, 35, 30, 25, 20, 15, 15, 25, 35, 45]  # [3], [4]Estimated additional cost per ton

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot percentage time saved
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Percentage Time Saved (%)', color='b', fontsize=12)
ax1.plot(months, percent_saved, marker='o', color='b', linestyle='-', linewidth=2, markersize=8, label='Time Saved (%)')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis for icebreaker costs
ax2 = ax1.twinx()
ax2.set_ylabel('Icebreaker Cost ($ per ton)', color='r', fontsize=12)
ax2.plot(months, icebreaker_cost_per_ton, marker='s', color='r', linestyle='--', linewidth=2, markersize=8, label='Icebreaker Cost ($/ton)')
ax2.tick_params(axis='y', labelcolor='r')

# Adding title and grid
plt.title('NSR vs. Suez Canal: Time Saved & Icebreaker Costs (2024)', fontsize=14)
ax1.grid(True, linestyle='--', linewidth=0.5)

# Show the plot
plt.show()

# Sources:
# [1] General distance savings of 30-50% on NSR vs Suez Canal.
# [2] NSR route is most efficient during summer (July-Sept), reaching 50% savings.
# [3] Icebreaker costs rise in winter due to delays and fuel consumption.
# [4] Icebreaker assistance can add $15–50 per ton based on ice conditions.
# [5] Transshipment costs are factored in Arctic port logistics.
