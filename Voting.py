## ============================= CLASSES ====================================

class Candidate:
    def __init__(self,candi_name):
        self.name = candi_name
        self.ballot_list = []
        self.count = 0

    def __str__(self):
        return self.name

class Ballot:
    def __init__(self,ballot_list):
        self.ballot_list = ballot_list
        # this index is used when revote; this is crutial, we call it marker
        self.index = 1
        
    # used when revote, to get next pref by voter
    def get_next(self,i):
        # make a copy
        j = i
        #i += 1
        self.index += 1
        return self.ballot_list[j]

    def revote(self,list_of_current_candis,list_of_elim_candis,ballot,dic_num_to_candi):
        assert type(list_of_current_candis) is list
        while True:
            candi_revote = dic_num_to_candi[int(self.get_next(self.index))]
            try:
                if ( candi_revote in list_of_current_candis):
                    candi = candi_revote
                    candi.count += 1
                    candi.ballot_list.append(ballot)
                    break
            except StopIteration:
                break
    
def has_winner(cutoff, cutoff_tie, list_of_current_candis):
    assert type(list_of_current_candis) is list
    assert cutoff >= 0

    all_tied = True
    max_v = 0
    min_v = 2 * cutoff
    for candi in list_of_current_candis:
        if (candi.count > max_v):
            max_v = candi.count
        if(candi.count < min_v):
            min_v = candi.count

    assert max_v >= 0
    assert min_v >= 0
 
    if(max_v >= cutoff):
        return True
    elif(max_v == min_v):
        return True

    return False


# =======================================================================
# ================================= CODE ==================================
# ================================================================

def voting_solve (r, w) :
    cases = r.readline() 
    blank = r.readline()

    for i in range(int(cases)):
        case_index = i
        num_ballots = 0

        l = r.readline()
        num_candis = int(l)
        assert num_candis >= 0

        list_of_current_candis = []
        list_of_elim_candis = []

        # dic_name_to_object {candidate_name:candi_object}
        # dic_num_to_candi {number:candi_object}
        dic_name_to_object = {}
        for i in range(num_candis):
            name = r.readline().rstrip()
            candi = Candidate(name)
            dic_name_to_object[str(name)] = candi
            list_of_current_candis.append(candi)
        
        list_of_items = zip(range(1,num_candis + 1),list_of_current_candis) # []
        # dic comprehension
        dic_num_to_candi = {k : v for k, v in list_of_items}

        list_of_ballots = [] 
        end = False   
        while (not end):
            line = r.readline().rstrip()
            if (line != ""):
                line_list = line.split()
                list_of_ballots.append(line_list)
            else:
                end = True

        # first round voting 
        for line in list_of_ballots:
            ballot = Ballot(line)
            first_choice = line[0]
            candi_object = dic_num_to_candi[int(first_choice)]
            candi_object.ballot_list.append(ballot)
            candi_object.count += 1
            num_ballots += 1

        # calculating majority cutoff
        if (num_ballots == 1):
            cutoff = 1
        elif (num_ballots % 2 == 0):
            cutoff = num_ballots / 2 + 1 
        else:
            cutoff = num_ballots //2 + 1
        assert cutoff >= 0

        # cycles until winner is found
        while (has_winner(cutoff, (num_ballots / num_candis),list_of_current_candis) == False):
            list_of_elim_candis = []
            current_candi_copy = list(list_of_current_candis)
            # first find the least num of ballots
            for candi in list_of_current_candis:
                if (candi.count == 0):
                    least_ballot = 0
                else:
                    least_ballot = list_of_current_candis[0].count
                    for candi in list_of_current_candis:
                        if (candi.count < least_ballot):
                            least_ballot = candi.count

            # for candidates with lowest number of votes
            for candi in current_candi_copy:
                if (candi.count == least_ballot):
                    list_of_elim_candis.append(candi)
                    list_of_current_candis.remove(candi)
            
            # bucket resorting cycle
            for candi in list_of_elim_candis:
                ballot_list = candi.ballot_list
                # go through each ballot in ballot_list (2D list)
                for ballot in ballot_list:
                    ballot.revote(list_of_current_candis,list_of_elim_candis,ballot,dic_num_to_candi)
                   
            num_candis = len(list_of_current_candis)
            assert num_candis >= 0
        
        # after a winner is found...

        all_tied = True
        for candi in list_of_current_candis:
            if (candi.count != num_ballots / num_candis):
                all_tied = False
                break

        # if tied winners
        if (all_tied == True):
            for candi in list_of_current_candis:
                print (candi)

        # if majority winner
        else:
            for candi in list_of_current_candis:
                if (candi.count >= cutoff):
                    print (candi)

        # bug: no blank line for last output line
        if (case_index != int(cases) - 1):
            print()

                  








