SELECT ?company ?companyLabel ?numberOfEmployees ?headquartersLocation ?headquartersLocationLabel ?revenue ?revenueYear ?foundingDate ?officialWebsite ?dissolutionDate ?netProfit ?marketCapitalization ?totalAssets
WHERE
{
    VALUES ?company
{wd: Q2283 wd: Q89 wd: Q182477 wd: Q3884 wd: Q679322 wd: Q713418 wd: Q217583 wd: Q2984214 wd: Q555925
 wd: Q9036}  # Пример компании: Wildberries (Q713418)

OPTIONAL
{
    SELECT ?company(MAX(?emp) AS ?numberOfEmployees) WHERE
{
?company
wdt: P1128 ?emp.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?location) AS ?headquartersLocation) WHERE
{
?company
wdt: P159 ?location.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?rev) AS ?revenue) (SAMPLE(?revYear)
AS ?revenueYear) WHERE
{
?company
p: P2139 ?revenueStatement.
?revenueStatement
ps: P2139 ?rev.
?revenueStatement
pq: P585 ?revYear.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(MAX(?foundDate) AS ?foundingDate) WHERE
{
?company
wdt: P571 ?foundDate.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?website) AS ?officialWebsite) WHERE
{
?company
wdt: P856 ?website.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(MAX(?dissDate) AS ?dissolutionDate) WHERE
{
?company
wdt: P576 ?dissDate.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?netProf) AS ?netProfit) WHERE
{
?company
wdt: P2295 ?netProf.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?marketCap) AS ?marketCapitalization) WHERE
{
?company
wdt: P2226 ?marketCap.
} GROUP
BY ?company
}

OPTIONAL
{
    SELECT ?company(SAMPLE(?assets) AS ?totalAssets) WHERE
{
?company
wdt: P2403 ?assets.
} GROUP
BY ?company
}

SERVICE
wikibase: label
{bd: serviceParam wikibase: language "[AUTO_LANGUAGE],en".}
}
