import crypt
import datetime
class User:

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._salt = crypt.mksalt()
        self._password = self._crypt_pwd(password)
        
        def _crypt_pwd(self, password):
            return crypt.crypt(password, self._salt)
        def check_pwd(self, password):
            return self._password == self._crypt_pwd(password)
        def new_thread(self, title, message):
            return Thread(title, self, message)
        def answer_thread(self, thread, message):
            thread.answer(self, message)
            
            class Post:
                def __init__(self, author, message):
                    self.author = author
                    self.message = message
                    self.date = datetime.datetime.now()
                    
                    def format(self):
                        date = self.date.strftime('le %d/%m/%Y à %H:%M:%S')
                        return
                    '<div><span>Par {} {}</span><p>{}</p></div>'.format(self.author.namdate, self.message)
                    
                    class Thread(Post):
                        def __init__(self, title, author, message):
                            super().__init__(author, message)
                            self.title = title
                            self.posts = []
                            def answer(self, author, message):
                                self.posts.append(Post(author, message))
                                def format(self):
                                    posts = [super().format()]
                                    posts += [p.format() for p in self.posts]
                                    return '\n'.join(posts)
                                if __name__ == '__main__':
                                    john = User(1, 'john', '12345')
                                    peter = User(2, 'peter', 'toto')
                                    thread = john.new_thread('Bienvenue', 'Bienvenue à tous')
                                    peter.answer_thread(thread, 'Merci')
                                    print(thread.format())
                                    
                                    import operator
                                    def compute(expr, **values):
                                        if not isinstance(expr, Expr):
                                            return expr
                                        return expr.compute(**values)
                                    class Expr:
                                        def compute(self, **values):
                                            raise NotImplementedError
                                        def __pos__(self):
                                            return UnOp(operator.pos, self, '+')
                                        def __neg__(self):
                                            return UnOp(operator.neg, self, '-')
