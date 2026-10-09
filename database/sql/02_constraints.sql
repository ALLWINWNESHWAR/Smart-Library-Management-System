-- ============================================================
-- SMART LIBRARY MANAGEMENT SYSTEM
-- File: 02_constraints.sql
-- Purpose: Additional business integrity constraints
-- ============================================================


-- ============================================================
-- 1. LOAN RETURN DATE CONSISTENCY
--
-- RETURNED loan  -> return_date must exist
-- ACTIVE/OVERDUE -> return_date must be NULL
-- ============================================================

ALTER TABLE loans
ADD CONSTRAINT ck_loans_return_date
CHECK (
    (status = 'RETURNED' AND return_date IS NOT NULL)
    OR
    (status IN ('ACTIVE', 'OVERDUE') AND return_date IS NULL)
);


-- ============================================================
-- END OF 02_constraints.sql
-- ============================================================

INSERT INTO loans (
    copy_id,
    member_id,
    issue_date,
    due_date,
    return_date,
    status
)
VALUES (
    1,
    1,
    SYSDATE,
    SYSDATE + 14,
    NULL,
    'RETURNED'
);


SELECT USER FROM dual;