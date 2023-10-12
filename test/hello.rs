fn main() {
     
}

fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    for i in 2..((n as f64).sqrt() as i32 + 1) {
        if n % i == 0 {
            return false;
        }
    }
    true
}
