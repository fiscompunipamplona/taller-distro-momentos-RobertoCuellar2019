class momentos:
    total = 0.
    total1 = 0.
    total2 = 0.
    media_pond = 0.
    def __init__(self):
        print ( "" )

    def m1(self, frec, bins, N):
        for i in range(len(bins)):
            self.total += bins[i]*frec[i]
        media_pond = self.total / N
        return (media_pond)
        
    def m2(self,frec , bins ,N):
        media = momentos()
        mediad = media.m1(bins, frec, N)
        const = N-1
        for j in range(len(bins)):
            self.total += frec[j]*((bins[j]-mediad) ** 2)
        varianza = self.total/(const)
        sigma = varianza ** 0.5
        for h in range(len(bins)):
            self.total1 += frec[h]*(((bins[h]-mediad)/sigma) ** 4)
            self.total2 += frec[h]*(((bins[h]-mediad)/sigma) ** 3)
        skew = ((self.total2)/N)
        curtosis = ((self.total1)/N) -3
        return ([varianza, sigma, skew, curtosis, mediad])
        
        

