# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

sentence1 = "Hi all, my name is Tom... I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def solution1(sentence):
  for p in ",.!?;:'":
    sentence = sentence.replace(p, "")
  words = sentence.split()

  sum = 0
  for word in words:
    sum += len(word)
  return round(sum/len(words), 2)


def solution2(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(map(len, words))/len(words), 2)


print(solution2(sentence1))
print(solution2(sentence2))

