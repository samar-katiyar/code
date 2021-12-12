morse_code_dict = {
    "-":"T",     ".":"E",     "--":"M",     "..":"I",     "-.":"N",
    ".-":"A",    "---":"O",   "--.":"G",    "-.-":"K",    "-..":"D",
    ".--":"W",   ".-.":"R",   "..-":"U",    "...":"S",    "-----":"0",
    "----.":"9", "--.-":"Q",  "--..":"Z",   "--...":"7",  "-.--":"Y",
    "-.-.":"C",  "-..-":"X",  "-...":"B",   "-....":"6",  ".---":"J",
    ".----":"1", ".--.":"P",  ".-..":"L",   "..---":"2",  "..-.":"F",
    "...-":"V",  "...--":"3", "....":"H",   "....-":"4",  ".....":"5"
}

def reverse_lookup(lookup_value):
    return [key for key, value in morse_code_dict.items() if value == lookup_value][0]

def decode_morse(sample_morse_code):
    morse_word_list = sample_morse_code.split('/')
    decoded_sentence=""
    for word in morse_word_list:
        decoded_word=""
        letters = word.split(' ')
        for letter in letters:
            decoded_word = decoded_word + morse_code_dict[letter]
        decoded_sentence = decoded_sentence + decoded_word + ' '    
    return decoded_sentence

def encode_morse(sample_code):
    word_list = sample_code.split(' ')
    encoded_sentence=""
    for word in word_list:
        encoded_word=""
        for letter in word:
            encoded_word = encoded_word + reverse_lookup(letter.upper()) + " "
        encoded_sentence = encoded_sentence + encoded_word[:-1] + "/"
    return encoded_sentence[:-1]
def main():
    print "Decoded Sentence ---> " + decode_morse("../.-.. --- ...- ./.--. .- .--. .-")
    print "Encoded Sentence ---> " + encode_morse("Papa is so cuddly")

if __name__=="__main__":
    main()