# **SubGPT 1.0**
<img width="943" alt="image" src="https://github.com/aalramadan/SubGPT/assets/55710790/81404e39-a31a-4b3f-b40e-0cf52e03851e">




## **What does it do?**
**SubGPT** provides translations for *multiple* languages using ChatGPT. 

## **ChatGPT Models Supported**

- **gpt-3.5-turbo**
- **gpt-4**


## **Features**

- **SubGPT** provides an option to specify the number of maximum input *tokens*. Higher number could lead to a better translation accuracy. Use according to your rate limit and subscription.

- You can *pause/resume* translation at any point.

- You can *remove* and/or *edit* the translated output and the input. The tool will automatically align the non-empty rows.

- Final output along with the modifications can be saved as an *.srt*

## **Experimental**
- SubGPT utilizes cosine similarity to compare the word embeddings between the input and final output using the *text-embedding-ada-002* model. A threshold between [-1, 1] where 1 indicates total semantic similarity and -1 indicates to semantic similarity at all.

- Higher tokens could lead to high translation accuracy, but may lead to incorrect alignments between the input and output. This option can fix the problem at the expense of using more tokens and time.


## **Demo**
![Animation](https://github.com/aalramadan/SubGPT/assets/55710790/529fc1c0-91a8-47f8-bee5-664a17b675ba)


## **Contribution**
You can open an issue to discuss any errors or bugs or for general enhancements and suggestions.

## **Disclaimer**
The SubGPT tool is an *experimental* tool provided for informational and educational purposes only. The accuracy and completeness of the output cannot be guaranteed. 

SubGPT is part of a collaborative research between *Ali Al-Ramadan* and *Hussein Abu-Rayyash* to provide not only accurate but culturally nuanced translations using cosine similarity.
