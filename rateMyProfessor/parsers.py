from utils.xpath import XPathParser, XpathField


class ProfessorRatingParser(XPathParser):

    fields = [
        XpathField(
            'courseName',
            './div/div[3]/div[1]/div[1]/div/text()',
            func=lambda t: ''.join(t).strip(),
        ),
        XpathField(
            'date',
            './div/div[3]/div[1]/div[2]/text()',
            single=True
        ),
        XpathField(
            'quality',
            './div/div[2]/div[1]/div/div[2]/text()',
            single=True
        ),
        XpathField(
            'difficulty',
            './div/div[2]/div[2]/div/div[2]/text()',
            single=True
        )
    ]


class ProfessorDetailPageParser(XPathParser):

    fields = [
        XpathField(
            'firstName',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[2]/div[1]/span[1]/text()',
            single=True),
        XpathField(
            'lastName',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[2]/div[1]/span[2]/text()',
            single=True),
        XpathField(
            'rating',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[1]/text()',
            single=True),
        XpathField(
            'takeAgainPercentage',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/text()',
            single=True),
        XpathField(
            'difficulty',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]/text()',
            single=True),
        XpathField(
            'school',
            '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[2]/div[2]/a/text()',
            single=True),
        XpathField(
            'ratings',
            '//*[@id="ratingsList"]/li/div[not(@id="ad-controller")]',
            func=lambda t: [ProfessorRatingParser().parse(e) for e in t],
        )

    ]
