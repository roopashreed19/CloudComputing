# Experiment 5: Implement a Mailing Service Using Apex Programming Language on Salesforce

## Aim

To implement a custom mailing service using the Apex programming language on Salesforce.

---

## Objectives

* To understand how to send emails programmatically in Salesforce Apex using the `Messaging` namespace.
* To create a reusable Apex class named `EmailManager` for sending emails.
* To test email execution through the Salesforce Developer Console using Anonymous Apex.
* To inspect execution debug logs and verify email delivery.

---

## Software / Platform Used

* **Platform:** Salesforce Cloud Platform
* **Environment:** Salesforce Developer Edition Org
* **Tool:** Salesforce Developer Console
* **Programming Language:** Apex
* **Namespace:** `Messaging`

---

## Procedure

### Step 1: Open the Developer Console

1. Log in to the Salesforce Developer Org.
2. From the top-right corner of the Salesforce dashboard, click the **Setup Gear Icon** ⚙️.
3. Select **Developer Console** from the dropdown menu.
4. The Salesforce Developer Console opens in a new window.

---

### Step 2: Create a New Apex Class

1. In the Developer Console top navigation bar, select:

   **File → New → Apex Class**

2. In the prompt box, enter the class name:

```text
EmailManager
```

3. Click **OK**.

A new Apex class named `EmailManager` is created.

---

### Step 3: Replace the Default Class Body

Replace the default generated class with the following Apex code:

```apex
public class EmailManager {
    
    // Public method to send a single email
    public static void sendMail(String address, String subject, String body) {
        
        // Create an instance of the SingleEmailMessage object
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
        
        // Define recipient address array
        String[] toAddresses = new String[] { address };
        mail.setToAddresses(toAddresses);
        
        // Set email subject and body content
        mail.setSubject(subject);
        mail.setPlainTextBody(body);
        
        // Send the email using Salesforce's built-in email service
        Messaging.SendEmailResult[] results = Messaging.sendEmail(
            new Messaging.SingleEmailMessage[] { mail }
        );
        
        // Inspect and log the email delivery result
        inspectResults(results);
    }
    
    // Helper method to inspect email sending results
    private static Boolean inspectResults(Messaging.SendEmailResult[] results) {
        
        Boolean sendResult = true;
        
        // Iterate through the results to verify delivery status
        for (Messaging.SendEmailResult res : results) {
            
            if (res.isSuccess()) {
                System.debug('Email sent successfully');
            } 
            else {
                sendResult = false;
                System.debug('The following errors occurred: ' + res.getErrors());
            }
        }
        
        return sendResult;
    }
}
```

---

## Code Breakdown

### 1. Create the Email Object

```apex
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
```

Creates a `SingleEmailMessage` object that represents the email to be sent.

---

### 2. Define the Recipient

```apex
String[] toAddresses = new String[] { address };
mail.setToAddresses(toAddresses);
```

Creates an array containing the recipient's email address and assigns it as the destination of the email.

---

### 3. Set the Subject

```apex
mail.setSubject(subject);
```

Sets the subject of the email.

---

### 4. Set the Email Body

```apex
mail.setPlainTextBody(body);
```

Sets the email body as plain text.

---

### 5. Send the Email

```apex
Messaging.SendEmailResult[] results = Messaging.sendEmail(
    new Messaging.SingleEmailMessage[] { mail }
);
```

Uses Salesforce's built-in `Messaging.sendEmail()` method to send the email.

The method returns a `SendEmailResult` array containing information about whether the email was successfully submitted or whether errors occurred.

---

### 6. Inspect the Result

```apex
inspectResults(results);
```

Calls the helper method to check the result of the email operation.

---

### 7. Check for Successful Delivery

```apex
if (res.isSuccess()) {
    System.debug('Email sent successfully');
}
```

Checks whether Salesforce successfully processed the email request.

If successful, the message:

```text
Email sent successfully
```

is written to the debug log.

---

## Step 4: Save the Apex Class

1. In the Developer Console, select:

   **File → Save**

2. Alternatively, press:

```text
Ctrl + S
```

3. The `EmailManager` Apex class is now saved and available for execution.

---

## Step 5: Execute the Apex Code Anonymously

1. In the Developer Console, select:

   **Debug → Open Execute Anonymous Window**

2. Alternatively, press:

```text
Ctrl + E
```

3. Enter the following code:

```apex
EmailManager.sendMail(
    'your_email@example.com',
    'Test Email Subject',
    'This is a test email sent from Salesforce Apex Email Service.'
);
```

Replace:

```text
your_email@example.com
```

with the email address where you want to receive the test email.

4. Make sure the **Open Log** checkbox is selected.
5. Click **Execute**.

---

## Step 6: Verify the Execution Output

After execution completes, the **Execution Log** window opens.

At the bottom of the log viewer:

1. Select the **Debug Only** filter.
2. Check the debug output generated by the Apex program.

If the email operation is successful, the log displays:

```text
Email sent successfully
```

The execution log confirms that Salesforce successfully processed the email request.

---

## Step 7: Verify the Email

Open the recipient email inbox.

Check for an email with the subject:

```text
Test Email Subject
```

The email body should contain:

```text
This is a test email sent from Salesforce Apex Email Service.
```

> **Note:** Email delivery can depend on Salesforce org email settings, verification requirements, and email deliverability configuration. A successful `Messaging.sendEmail()` result indicates that Salesforce accepted the email request; it does not by itself guarantee final inbox delivery.

---

## Complete Apex Program

The complete `EmailManager` class used in this experiment is:

```apex
public class EmailManager {
    
    public static void sendMail(String address, String subject, String body) {
        
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();
        
        String[] toAddresses = new String[] { address };
        mail.setToAddresses(toAddresses);
        
        mail.setSubject(subject);
        mail.setPlainTextBody(body);
        
        Messaging.SendEmailResult[] results = Messaging.sendEmail(
            new Messaging.SingleEmailMessage[] { mail }
        );
        
        inspectResults(results);
    }
    
    private static Boolean inspectResults(Messaging.SendEmailResult[] results) {
        
        Boolean sendResult = true;
        
        for (Messaging.SendEmailResult res : results) {
            
            if (res.isSuccess()) {
                System.debug('Email sent successfully');
            } 
            else {
                sendResult = false;
                System.debug('The following errors occurred: ' + res.getErrors());
            }
        }
        
        return sendResult;
    }
}
```

---

## Anonymous Apex Code Used for Testing

```apex
EmailManager.sendMail(
    'your_email@example.com',
    'Test Email Subject',
    'This is a test email sent from Salesforce Apex Email Service.'
);
```

---

## Important Concepts

### Salesforce Messaging Namespace

The `Messaging` namespace provides Apex classes and methods for sending emails from Salesforce.

### `Messaging.SingleEmailMessage`

Represents an individual email message that can be sent from Apex.

### `setToAddresses()`

Specifies the email address or addresses of the recipients.

### `setSubject()`

Sets the subject line of the email.

### `setPlainTextBody()`

Sets the email content as plain text.

### `Messaging.sendEmail()`

Submits the email message for sending through Salesforce's email service.

### `System.debug()`

Writes information to the Salesforce execution log, which can be used to verify execution and troubleshoot errors.

---

## Result

The `EmailManager` Apex class was successfully created and saved in the Salesforce Developer Org.

The class was executed using Anonymous Apex in the Developer Console. The `Messaging.sendEmail()` method was used to submit a test email, and the execution result was inspected through the Debug Log.

The test email was successfully processed and could be verified in the recipient's email inbox, subject to Salesforce email deliverability settings.

---

## Conclusion

This experiment demonstrated how to implement a custom mailing service using Apex on the Salesforce cloud platform.

The `Messaging` namespace and `SingleEmailMessage` class were used to create and send an email programmatically. The experiment also demonstrated how Anonymous Apex can be used to test the mailing service and how Debug Logs can be used to inspect the execution result.
