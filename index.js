const { createScraper } = require("israeli-bank-scrapers");
const fs = require("fs");
const process = require("process");

async function start(user, pass, bank) {
    const credentials = { username: user, password: pass };
    const options = { companyId: bank};
    const scraper = createScraper(options);
    const scrapeResult = await scraper.scrape(credentials);

    if (scrapeResult.success) {
        scrapeResult.accounts.forEach(account => {
            console.log(
                `found ${account.txns.length} transactions for account number ${account.accountNumber}`
            );
        });
        fs.writeFileSync("accounts.json", JSON.stringify(scrapeResult));
        process.exit(0);
    } else {
        console.error(
            `scraping failed for the following reason: ${scrapeResult.errorType}`
        );
        process.exit(1);
    }
}

if (process.argv.length !== 5) {
    console.error("Usage: node index.js [user] [pass] [bank]");
    console.error(
        "bank could be one of: 'hapoalim', 'leumi', 'discount', 'otsarHahayal', 'visaCal', 'leumiCard', 'isracard', 'amex'"
    );
}

start(process.argv[2], process.argv[3], process.argv[4])
    .then(() => console.log("done"))
    .catch(ex => console.error(ex));
