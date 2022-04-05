package banking;

import java.util.HashMap;

/**
 * Private Variables:<br>
 * {@link #accounts}: List&lt;Long, Account&gt;
 */
public class Bank implements BankInterface {
	private HashMap<Long, Account> accounts;
	private long accountNumber = 0L;

	public Bank() {
		this.accounts = new HashMap<Long, Account>();
	}

	private Account getAccount(Long accountNumber) {
		if(accounts.containsKey(accountNumber)) {
			return this.accounts.get(accountNumber);
		}
        return null;
	}

	public Long openCommercialAccount(Company company, int pin, double startingDeposit) {
		Long accountNumber = ++this.accountNumber;
		CommercialAccount commercialAccount = new CommercialAccount(company, accountNumber, pin, startingDeposit);
		accounts.put(accountNumber, commercialAccount);
		return accountNumber;
	}

	public Long openConsumerAccount(Person person, int pin, double startingDeposit) {
		Long accountNumber = ++this.accountNumber;
		ConsumerAccount consumerAccount = new ConsumerAccount(person, accountNumber, pin, startingDeposit);
		accounts.put(accountNumber, consumerAccount);
		return accountNumber;
	}

	public boolean authenticateUser(Long accountNumber, int pin) {
		Account account = getAccount(accountNumber);
		if (account != null) {
			return account.validatePin(pin);
		}
        return false;
	}

	public double getBalance(Long accountNumber) {
		Account account = getAccount(accountNumber);
		if (account != null) {
			return account.getBalance();
		}
        return -1;
	}

	public void credit(Long accountNumber, double amount) {
		Account account = getAccount(accountNumber);
		if (account != null) {
			account.creditAccount(amount);
		}
	}

	public boolean debit(Long accountNumber, double amount) {
		Account account = getAccount(accountNumber);
		if (account != null) {
			return account.debitAccount(amount);
		}
        return false;
	}
}
