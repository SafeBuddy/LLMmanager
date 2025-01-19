prompt = (
    "Analyze the following text for evidence of verbal abuse or grooming. If either is present, identify:\n"
    "1. Who is the aggressor and who is the victim.\n"
    "2. Assign a severity score from 0 to 2 based on the intensity and frequency of the behavior, where:\n"
    "0: No abuse or grooming.\n"
    "1: Moderate (repeated behavior, potentially harmful).\n"
    "2: Severe (persistent or highly damaging behavior, significant impact).\n"
    "Please return the answer in valid JSON format as follows:\n"
    "{\n"
    "  \"aggressor\": \"[Insert aggressor’s name or identifier here, or write null if there is no one]\",\n"
    "  \"severity\": [Insert numerical score here]\n"
    "}\n"
    "Only return valid JSON, with no additional text or commentary."
)
