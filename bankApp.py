# 1. Scanner Import
import java.util.Scanner;

# 2. Bank App Suite
public class BankApplication {

# 2.1 User Initial Prompts (Home screen)
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your 'Name' and 'CustomerId' to access your Bank account:");
        String name=sc.nextLine();
        String customerId=sc.nextLine();
        BankAccount obj1=new BankAccount(name,customerId);
        obj1.menu();
    }
}

# 2.2 Bank Account Status
# 2.2.1 Balances & Recent Transactions
class BankAccount{
  double bal;
  double prevTrans;
  String customerName;
  String customerId;
  
  # 2.2.2 Bank Customer Information
  BankAccount(String customerName,String customerId){
    this.customerName=customerName;
    this.customerId=customerId;
    }
}
