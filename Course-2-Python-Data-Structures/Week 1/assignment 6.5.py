#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";

ipos = text.find(':')
trim = text[ipos+1:]
value = float(trim)
print(value)