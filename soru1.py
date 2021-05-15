void
reverse_words()
{

-
char
words[10][20] = {" "};
int
i;
printf("Bir cumle giriniz: ");
gets(sentence);
int
word_counter = 0;
int
word_letter_counter = 0;
for (i=0;i <= strlen(sentence);
i + +){
if (sentence[i] == ' ' | | sentence[i] == '\0')
{
    words[word_counter][word_letter_counter] = '\0';
word_letter_counter = 0;
word_counter + +;
}
else {
    words[word_counter][word_letter_counter] = sentence[i];
word_letter_counter + +;
}
}
int
j;
for (j=word_counter;j >= 0;j--)
{
    printf(" %s ", words[j]);
}

}
