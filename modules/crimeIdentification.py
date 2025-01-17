import json

MIN_COINCIDENCES = 2


class CrimeCategorization:

    def get_crime_keywords(self, keywords_file):
        with open(keywords_file) as file:
            crimes = json.load(file)
            return crimes

    def identification(self, topic_analysis, keywords):
        print("Identifying...")
        crimes = keywords
        lang = topic_analysis['lang']
        topic = topic_analysis['topic']
        is_delit = False
        art_crimes = []
        for art in crimes.keys():
            count_coincidences = 0
            keywords = crimes.get(art)[lang]
            for k in keywords:
                if k in topic:
                    count_coincidences += 1
                    if count_coincidences >= MIN_COINCIDENCES:
                        art_crimes.append(art)
                        is_delit = True
                        print("Encontrado"+art)
                        break
        print("Crimes: "+','.join(art_crimes))
        return [
            ','.join(topic_analysis['topic']),
            ','.join(art_crimes),
            is_delit,
            topic_analysis['id']
        ]
