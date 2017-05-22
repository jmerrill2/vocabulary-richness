from nltk.stem.porter import PorterStemmer
from itertools import groupby


def words(entry):
    words = filter(lambda w: len(w) > 0, [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])
    return words


def yule(entry):
    # yule's I measure (the inverse of yule's K measure)
    # higher number is higher diversity - richer vocabulary
    d = {}
    stemmer = PorterStemmer()
    for w in words(entry):
        w = stemmer.stem(w).lower()
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1

    M1 = float(len(d))
    M2 = sum([len(list(g)) * (freq ** 2) for freq, g in
              groupby(sorted(d.values()))])

    try:
        val = (M1 * M1) / (M2 - M1)
        print('val: ', val)
        return val
    except ZeroDivisionError:
        print('OOPS, division by 0 error.')
        return 0


if __name__ == '__main__':
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    text = """
    sure and displeasure and the will, which are not cognitions at all) contains
    nothing but mere relations,a of places in one intuition (extension),
    alteration of places (motion), and laws in accordance with which this al- B 67
    teration is determined (moving forces). But what is present in the place,
    or what it produces in the things themselves besides the alteration of
    place, is not given through these relations. Now through mere relations
    no thing in itself is cognized; it is therefore right to judge that since
    nothing is given to us through outer sense except mere representations
    of relation, outer sense can also contain in its representation only the
    relation of an object to the subject, and not that which is internal to the
    objectb in itself.36 It is exactly the same in the case of inner sense. It is
    not merely that the representations of outer sense make up the proper
    material with which we occupy our mind, but also the time in which we
    place these representations, which itself precedes the consciousness of
    them in experience and grounds the way in which we place them in
    mind as a formal condition, already contains relations of succession, of
    simultaneity, and of that which is simultaneous with succession (of that
    which persists). Now that which, as representation, can precede any act
    of thinking something is intuition and, if it contains nothing but relations,
    it is the form of intuition, which, since it does not represent anything
    except insofar as something is posited in the mind, can be nothing
    other than the way in which the mind is affected by its own activity,
    namely this positing of its representation, thus the way it is affected B 68
    through itself, i.e., it is an inner sense as far as regards its form.
    Everything that is represented through a sense is to that extent always
    appearance, and an inner sense must therefore either not be admitted at
    all or else the subject, which is the object of this sense, can only be represented
    by its means as appearance, not as it would judge of itself if its
    intuition were mere self-activity, i.e., intellectual. Any difficulty in this
    depends merely on the question how a subject can internally intuit itself;
    yet this difficulty is common to every theory. Consciousness of itself
    (apperception) is the simple representation of the I, and if all of the
    manifold in the subject were given self-actively through that alone,
    then the inner intuition would be intellectual. In human beings this
    consciousness requires inner perception of the manifold that is antecedently
    given in the subject, and the manner in which this is given in
    the mind without spontaneity must be called sensibility on account of
    this difference. If the faculty for becoming conscious of oneself is to
    seek out (apprehend) that which lies in the mind, it must affect the lat    
    """

    yule(text)
