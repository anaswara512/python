words=['apple','banana','apple','orange','banana','apple']
result={word:words.count(word) for word in set(words)}
print(result)