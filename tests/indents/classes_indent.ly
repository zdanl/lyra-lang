struct Admin(User):
    def kick(user_name):int
        pass
    }
    def ban(user_name):int
        pass
    }

struct Op(User)
    def kick(user_name):int
        pass

    def ban(user_name):int
        pass


struct User() {

    nick = ""

    def say(room_name, message):int{

    }
    def poke(user_name):int{

    }
}

def main():int{

    user1 = User()
    user2 = User()
    admin1 = Admin()
    admin2 = Admin()
    user1.say("nerds", "hello")
    user2.poke(user1)
    admin1.kick(user1.nick)
    admin1.ban(user2.nick)
    if admin2.kick(admin1) > 0 {
        /* error admins can not kick admins */
    }

    return 0
}
