from io import StringIO
from unittest import main,TestCase
from Voting import voting_solve,has_winner,Candidate,Ballot

class TestVoting(TestCase):

    def test_has_winner_1(self):
    	candi = Candidate("candi")
    	candi_2 = Candidate("candi_2")
    	list_1 = [candi, candi_2]
    	a = has_winner(3, 2.5, list_1)
    	self.assertEqual(a, True)
    def test_has_winner_2(self):
    	a = has_winner(1, .25, ["Red", "Green", "Blue", "Orange"])
    	self.assertEqual(a, True)
    def test_has_winner_3(self):
    	a = has_winner(9, 2, ["C1", "C2", "C3", "C4"])
    	self.assertEqual(a, True)
    def test_has_winner_4(self):
    	a = has_winner(5, 2, ["1", "2", "3"])
    	self.assertEqual(a, False)



    def test_Candidate_class1(self):
        p = Candidate("a")
        self.assertEqual(p.name, "a")
        self.assertEqual(p.count,0)
        self.assertEqual(p.ballot_list,[])

    def test_Candidate_class2(self):
        p = Candidate("b")
        self.assertEqual(p.name, "b")
        self.assertEqual(p.count,0)
        self.assertEqual(p.ballot_list,[]) 


    def test_Candidate_class3(self):
        p = Candidate("c")
        self.assertEqual(p.name, "c")
        self.assertEqual(p.count,0)
        self.assertEqual(p.ballot_list,[])







    # below are test for ballot class
    def test_Ballot_class1(self):
        ballot = Ballot([1,2,3])
        self.assertEqual(ballot.get_next(1),2)

    def test_Ballot_class2(self):
        ballot = Ballot([1,2,3])
        self.assertEqual(ballot.get_next(0),1)

    def test_Ballot_class3(self):
        ballot = Ballot([1,2,3])
        self.assertEqual(ballot.get_next(2),3)


    def test_Ballot_class4(self):
        ballot = Ballot([5,6,7])
        self.assertEqual(ballot.get_next(0),5)

    def test_Ballot_class5(self):
        ballot = Ballot([5,6,7])
        self.assertEqual(ballot.get_next(1),6)

    def test_Ballot_class6(self):
        ballot = Ballot([5,6,7])
        self.assertEqual(ballot.get_next(2),7)








    def test_haswinner1(self):
        self.assertEqual(has_winner(5, 1, [Candidate("a")]),True)


    def test_haswinner2(self):
        self.assertEqual(has_winner(4, 1, [Candidate("b")]),True)

    def test_haswinner3(self):
        self.assertEqual(has_winner(3, 1, [Candidate("c")]),True)


    def test_haswinner4(self):
        self.assertEqual(has_winner(7, 1, [Candidate("d")]),True)

    def test_haswinner5(self):
        self.assertEqual(has_winner(8, 1, [Candidate("e")]),True)





    def test_votingsolve(self):
        jo = Candidate("jo")
        ja = Candidate("ja")
        r = StringIO("1\n\n2\nJo\nJa\n2 1\n2 1")
        w = StringIO()
        self.assertEqual(voting_solve(r,w),None)

    def test_votingsolve1(self):
        jo = Candidate("jo")
        ja = Candidate("ja")
        Ss = Candidate("Ss")
        r = StringIO("1\n\n3\nJo\nJa\nSs\n1 2 3\n2 1 3\n2 3 1\n1 2 3\n3 1 2")
        w = StringIO()
        self.assertEqual(voting_solve(r,w),None)





main()

