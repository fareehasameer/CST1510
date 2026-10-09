total_seconds=9137
hours=total_seconds//3600
remainder=total_seconds%3600

minutes=remainder//60
seconds=remainder%60

print(total_seconds,"is equal to",hours,"hours,",minutes,"minutes and",seconds,"seconds.")
