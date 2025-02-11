from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from langfuse.callback import CallbackHandler


information = """
India, officially the Republic of India (ISO: Bhārata Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.

Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[28][29][30] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[31] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[32] By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[33][34] Its evidence today is found in the hymns of the Rigveda. Preserved by an oral tradition that was resolutely vigilant, the Rigveda records the dawning of Hinduism in India.[35] The Dravidian languages of India were supplanted in the northern and western regions.[36] By 400 BCE, stratification and exclusion by caste had emerged within Hinduism,[37] and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity.[38] Early political consolidations gave rise to the loose-knit Maurya and Gupta Empires based in the Ganges Basin.[39] Their collective era was suffused with wide-ranging creativity,[40] but also marked by the declining status of women,[41] and the incorporation of untouchability into an organised system of belief.[k][42] In South India, the Middle kingdoms exported Dravidian-languages scripts and religious cultures to the kingdoms of Southeast Asia.[43]

In the early medieval era, Christianity, Islam, Judaism, and Zoroastrianism became established on India's southern and western coasts.[44] Muslim armies from Central Asia intermittently overran India's northern plains,[45] eventually founding the Delhi Sultanate, and drawing northern India into the cosmopolitan networks of medieval Islam.[46] In the 15th century, the Vijayanagara Empire created a long-lasting composite Hindu culture in south India.[47] In the Punjab, Sikhism emerged, rejecting institutionalised religion.[48] The Mughal Empire, in 1526, ushered in two centuries of relative peace,[49] leaving a legacy of luminous architecture.[l][50] Gradually expanding rule of the British East India Company followed, turning India into a colonial economy, but also consolidating its sovereignty.[51] British Crown rule began in 1858. The rights promised to Indians were granted slowly,[52][53] but technological changes were introduced, and modern ideas of education and the public life took root.[54] A pioneering and influential nationalist movement emerged, which was noted for nonviolent resistance and became the major factor in ending British rule.[55][56] In 1947 the British Indian Empire was partitioned into two independent dominions,[57][58][59][60] a Hindu-majority Dominion of India and a Muslim-majority Dominion of Pakistan, amid large-scale loss of life and an unprecedented migration.[61]

India has been a federal republic since 1950, governed through a democratic parliamentary system. It is a pluralistic, multilingual and multi-ethnic society. India's population grew from 361 million in 1951 to almost 1.4 billion in 2022.[62] During the same time, its nominal per capita income increased from US$64 annually to US$2,601, and its literacy rate from 16.6% to 74%. From being a comparatively destitute country in 1951,[63] India has become a fast-growing major economy and a hub for information technology services, with an expanding middle class.[64] India has a space programme with several planned or completed extraterrestrial missions. Indian movies, music, and spiritual teachings play an increasing role in global culture.[65] India has substantially reduced its rate of poverty, though at the cost of increasing economic inequality.[66] India is a nuclear-weapon state, which ranks high in military expenditure. It has disputes over Kashmir with its neighbours, Pakistan and China, unresolved since the mid-20th century.[67] Among the socio-economic challenges India faces are gender inequality, child malnutrition,[68] and rising levels of air pollution.[69] India's land is megadiverse, with four biodiversity hotspots.[70] Its forest cover comprises 21.7% of its area.[71] India's wildlife, which has traditionally been viewed with tolerance in India's culture,[72] is supported among these forests, and elsewhere, in protected habitats.
"""

if __name__ == "__main__":
    print("Hello Langchain..")

    langfuse_handler = CallbackHandler(
        secret_key="",
        public_key="",
        #host="https://cloud.langfuse.com",  # 🇪🇺 EU region
        host="https://us.cloud.langfuse.com", # 🇺🇸 US region
    )

    summary_template = """
    given the information {information} I want you to give me the boundaries of India
    """

    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
    )

    llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm

    # Corrected invocation
    result = chain.invoke(
        {"information": information}, config={"callbacks": [langfuse_handler]}
    )
