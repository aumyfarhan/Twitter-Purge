from watson_developer_cloud import NaturalLanguageUnderstandingV1

import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='064250f8-3288-4246-a86e-123a130cd2b9',
  password='6QovBBP1nINY',
  version='2017-02-27')


response2 = natural_language_understanding.analyze(
        text=kkk2, 
        features=Features(
      entities=EntitiesOptions(
        emotion=True,
        sentiment=True)))


total_sum=0
cc=0
for x in response2.result['entities']:
    total_sum=total_sum+x['sentiment']['score']

final_score=total_sum/len(response2.result['entities'])
prtint(final_score)
