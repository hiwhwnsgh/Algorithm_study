-- 코드를 입력하세요
SELECT concat('/home/grep/src/',A.BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD A left join USED_GOODS_FILE B
on A.BOARD_ID = B.BOARD_ID
where VIEWS = (
    select max(VIEWS)
    from USED_GOODS_BOARD
)
order by B.FILE_ID DESC