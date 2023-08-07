Controllers/Subscription.py

class Subscription:
    def upgradeSubscription(session):
        return Account.upgrade(Auth.user("bearer", session['uid']))