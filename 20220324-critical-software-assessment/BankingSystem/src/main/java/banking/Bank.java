package banking;

import java.util.LinkedHashMap;

/**
 * Private Variables:<br>
 * {@link #accounts}: List&lt;Long, Account&gt;
 */
public class Bank implements BankInterface {
	private LinkedHashMap<Long, Account> accounts;

	public Bank() {
		this.accounts = new LinkedHashMap<Long, Account>();
	}

	private Account getAccount(Long accountNumber) {
		if(accounts.containsKey(accountNumber)) {
			return this.accounts.get(accountNumber);
		}
        return null;
	}

	public Long openCommercialAccount(Company company, int pin, double startingDeposit) {
		Long accountNumber = (long) (accounts.size() + 1);
		CommercialAccount commercialAccount = new CommercialAccount(company, accountNumber, pin, startingDeposit);
		accounts.put(accountNumber, commercialAccount);
		return accountNumber;
	}

	public Long openConsumerAccount(Person person, int pin, double startingDeposit) {
		Long accountNumber = (long) (accounts.size() + 1);
		ConsumerAccount consumerAccount = new ConsumerAccount(person, accountNumber, pin, startingDeposit);
		accounts.put(accountNumber, consumerAccount);
		return accountNumber;
	}

	public boolean authenticateUser(Long accountNumber, int pin) {
		if (accounts.containsKey(accountNumber)) {
			Account account = accounts.get(accountNumber);
			return account.validatePin(pin);
		}
        return false;
	}

	public double getBalance(Long accountNumber) {
		if (accounts.containsKey(accountNumber)) {
			return accounts.get(accountNumber).getBalance();
		}
        return -1;
	}

	public void credit(Long accountNumber, double amount) {
		if (accounts.containsKey(accountNumber)) {
			accounts.get(accountNumber).creditAccount(amount);
		}
	}

	public boolean debit(Long accountNumber, double amount) {
		if (accounts.containsKey(accountNumber)) {
			return accounts.get(accountNumber).debitAccount(amount);
		}
        return false;
	}
}
