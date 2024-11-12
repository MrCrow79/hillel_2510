registered_users = {'Den', 'Alex', 'Mor'}
invited_users = {'Den', 'Mor', 'Ivan', 'Sofia'}

user_with_invites_registered =  registered_users.intersection(invited_users)
print(user_with_invites_registered)

only_invited_without_registrations = invited_users.difference(registered_users)
only_registered_without_invites = registered_users.difference(invited_users)

print(only_invited_without_registrations)
print(only_registered_without_invites)

diff_between_2_sets = registered_users.symmetric_difference(invited_users)
print(diff_between_2_sets)

res = diff_between_2_sets.update(user_with_invites_registered) == registered_users.update(invited_users)
print(res)