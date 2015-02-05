
def get_missing_letters(sentance):
  """
  Determine if a string 'sentance' is a pangram.
  
  Returns a list of characters preventing 
  the string 'sentance' from being a pangram.
  """
  # Setup the metric for counting characters.
  chars = list("abcdefghijklmnopqrstuvwxyz")
  zeros = [0 for i in range(len(chars))]
  metric = dict(zip(chars, zeros))
  
  for char in sentance:
    # Increment corresponding value if key exists.
    charLower = char.lower()
    if metric.has_key(charLower):
      metric[charLower] += 1
  
  # Now, keys with a value of zero implies that
  # the character did not exist in the sentance.
  # Here, keys with a value more than 1 is removed
  # from the dictionary.
  kkeys = metric.keys()
  for k in kkeys:
    if metric[k] > 0:
      metric.pop(k)
  
  # Return missing characters from string 'sentance'.
  return "".join(sorted(metric.keys()))


if __name__ == "__main__":
  pass
