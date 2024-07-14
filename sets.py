def sets():
    def set_functions():
        st={1,23,4,5,3} #each value in a set are unique
        print(st)
        st.add(3)
        print(st) #even if there are duplicates it is automatically removed and made unique
        my_set={1,2,3,4,5,6,7,8,9}
        your_set={7,8,9,10,11,12,13}
        his_set={14,15,16,17,18,19,20}

        print(my_set.difference(your_set))
        print(your_set.difference(my_set)) #values unique in your_set in comparison to my set
        print(my_set.intersection(your_set)) #values present in both sets

        my_set.discard(8) #delete an item from the set
        print(my_set)

        my_set.difference_update(your_set)#items different from your_set are removed
        print(my_set)
        print(my_set.isdisjoint(your_set))#if both sets are completely different then returns True else False

        print(my_set.union(your_set))  #shows all values in both sets , doesn't actually modify the sets
        print(my_set)#not modified

        new_set={1,2,3}
        print(new_set.issubset(my_set)) #is new_set a subset of my_set

        print(my_set.issuperset(new_set)) #is my_set a subset of new_set? true if Yes else false
    set_functions()
sets()