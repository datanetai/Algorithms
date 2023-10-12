public class Primes{
    public static void main(String[] args){
        int n = Integer.parseInt(args[0]);
        if(prime(n))
            System.out.println(n + " is prime");
        else
            System.out.println(n + " is not prime");
        int[] factors = prime_factors(n);
        System.out.println("Prime factors of " + n + " are: ");
        for(int i=0; i<factors.length; i++){
            if(factors[i] != 0)
                System.out.print(factors[i] + " ");
        }
        System.out.println();
        int[] primes = sieve(n);
        System.out.println("Primes less than " + n + " are: ");
        for(int i=0; i<primes.length; i++){
            if(primes[i] != 0)
                System.out.print(primes[i] + " ");
        }

    }

    public static boolean prime(int n){
        if (n == 2)
            return true; 
        else if(n<1 || n%2 == 0)
            return false;

        for(int i=3; i*i<=n; i+=2){
            if(n%i == 0)
                return false;
        }
        return true;
    }

public static int[] prime_factors(int n){
    int d = 2;
    int[] factors = new int[100];
    int i = 0;
    while (n > 1){
        while (n % d == 0){
            factors[i] = d;
            i++;
            n = n/d;
        }
        d = d + 1;
    }
    return factors;
     
}
public static int[] sieve(int n){
    int[] primes = new int[n];
    primes[0] = 0; 
    primes[1] = 0; 
    for(int i=0; i<n; i++){
        primes[i] = i;
    }
    for(int i=2; i<n; i++){
        if(primes[i] != 0){
            for(int j=2*i; j<n; j+=i){
                primes[j] = 0;
            }
        }
    }
    return primes;
}
}