# Section 8: IPv6

## 1. Overview
* **Address Space Expansion:** To solve IPv4 address exhaustion, IPv6 expands address size from **32 bits to 128 bits**.
* **Massive Capacity:** Provides 2^128 possible addresses (a lot).

---

## 2. Address Representation
* **Colons-and-Hex Notation:**8 groups of 4 hexadecimal digits separated by colons (e.g., `2001:0db8:6ffa:8939:163b:4cab:98bf:070a`).
* **Slash Notation & Subnets:** Uses slash notation like IPv4; `/64` is the strongly recommended standard for host subnets.
* **Compression Rules:**
  1. **Remove leading zeros** in any 16-bit hexadecimal block (e.g., `0db8` becomes `db8`) [5].
  2. **Replace consecutive zero blocks** with double colons `::` (e.g., `2001:db8:6ffa:0:0:ab:98bf:70a` becomes `2001:db8:6ffa::ab:98bf:70a`) [5].

---

## 3. Link-Local Addresses
* **Subnet:** Reserved on subnet `fe80::/10` [6, 7].
* **Automatic Configuration:** Automatically assigned using its MAC address and other details.
* **Scope:** Unique only within the local LAN.

---

## 4. Special Addresses & Subnets
* **`::1`:** Localhost.
* **`2001:db8::/32`:** documentation and example code.
* **`fe80::/10`:** link-local addresses.

---

## 5. IPv6 with DNS & URLs
* **DNS Records:** IPv6 addresses are mapped in DNS using **`AAAA` records** (e.g., queried via `dig example.com AAAA`).
* **URL Syntax:** IPv6 addresses must be enclosed in **square brackets** when placed in a web browser (e.g., `http://[::1]:33490/`).
