---------------------------create ousi_staff-------------

-- ���� ousi_staff ��
create table ousi_staff(
       sid number primary key,  
       department varchar2(8),
       name varchar2(8),
       password varchar2(8),
       phone varchar2(11),
       role varchar2(8)
);
-- ���� seq_ousi_staff ����
create sequence seq_ousi_staff;

-- ���� tg_ousi_staff ������
create or replace trigger tg_ousi_staff before
  INSERT ON ousi_staff FOR EACH row
DECLARE integrity_error EXCEPTION;
  errno  INTEGER;
  errmsg CHAR(200);
  dummy  INTEGER;
  found  BOOLEAN;
BEGIN
  --  Column sid uses sequence seq_ousi_staff
  SELECT seq_ousi_staff.NEXTVAL
  INTO :new.sid -- ע�� id ������
  FROM dual;
  --  Errors handling

EXCEPTION
WHEN integrity_error THEN
  raise_application_error(errno, errmsg);
END;
/