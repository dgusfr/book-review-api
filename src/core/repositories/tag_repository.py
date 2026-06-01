from sqlmodel import desc, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.models.tag_model import Tag


class TagRepository:
    async def get_all(self, session: AsyncSession):
        statement = select(Tag).order_by(desc(Tag.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_by_uid(self, tag_uid: str, session: AsyncSession) -> Tag | None:
        statement = select(Tag).where(Tag.uid == tag_uid)
        result = await session.exec(statement)
        return result.first()

    async def get_by_name(self, name: str, session: AsyncSession) -> Tag | None:
        statement = select(Tag).where(Tag.name == name)
        result = await session.exec(statement)
        return result.first()

    async def create(self, tag: Tag, session: AsyncSession) -> Tag:
        session.add(tag)
        await session.commit()
        await session.refresh(tag)
        return tag

    async def update(self, tag: Tag, update_data: dict, session: AsyncSession) -> Tag:
        for key, value in update_data.items():
            setattr(tag, key, value)

        await session.commit()
        await session.refresh(tag)
        return tag

    async def delete(self, tag: Tag, session: AsyncSession) -> None:
        await session.delete(tag)
        await session.commit()
