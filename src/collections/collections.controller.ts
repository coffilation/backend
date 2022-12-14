import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
  Query,
  UseGuards,
  HttpCode,
  ParseIntPipe,
  Put,
} from '@nestjs/common'
import { CollectionsService } from './collections.service'
import { CreateCollectionDto } from './dto/create-collection.dto'
import { UpdateCollectionDto } from './dto/update-collection.dto'
import { ApiBearerAuth, ApiTags } from '@nestjs/swagger'
import { JwtUserId } from 'common/decorators/user.decorator'
import { JwtAuthGuard } from 'auth/guards/jwt-auth.guard'
import { UpdateCollectionPlacesDto } from 'collections/dto/update-collection-places.dto'
import { UnsafeExtractUserJwtAuthGuard } from 'auth/guards/unsafe-extract-user-jwt-auth.guard'
import { GetCollectionsQueryDto } from './dto/get-collections-query.dto'

@ApiTags(`collections`)
@Controller('collections')
export class CollectionsController {
  constructor(private readonly collectionsService: CollectionsService) {}

  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  @Post()
  create(
    @Body() createCollectionDto: CreateCollectionDto,
    @JwtUserId() authorId: number,
  ) {
    return this.collectionsService.create(createCollectionDto, authorId)
  }

  @ApiBearerAuth()
  @UseGuards(UnsafeExtractUserJwtAuthGuard)
  @Get()
  findAll(
    @JwtUserId() jwtUserId: number,
    @Query() query: GetCollectionsQueryDto,
  ) {
    return this.collectionsService.findAll(jwtUserId, query)
  }

  @ApiBearerAuth()
  @UseGuards(UnsafeExtractUserJwtAuthGuard)
  @Get(':id')
  findOne(@Param('id', ParseIntPipe) id: number, @JwtUserId() userId: number) {
    return this.collectionsService.findOne(id, userId)
  }

  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  @Put(':id/places')
  updatePlaces(
    @Param('id', ParseIntPipe) id: number,
    @Body() collectionPlacesDto: UpdateCollectionPlacesDto,
    @JwtUserId() jwtUserId: number,
  ) {
    return this.collectionsService.updateCollectionPlaces(
      jwtUserId,
      id,
      collectionPlacesDto,
    )
  }

  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  @Patch(':id')
  update(
    @Param('id', ParseIntPipe) id: number,
    @Body() updateCollectionDto: UpdateCollectionDto,
    @JwtUserId() userId: number,
  ) {
    return this.collectionsService.update(id, updateCollectionDto, userId)
  }

  // @Post(':id/join')
  // join(@Param('id') id: string, @JwtUserId() user) {
  //   return this.collectionsService.join(+id, user)
  // }

  @HttpCode(204)
  @Delete(':id')
  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  remove(
    @Param('id', ParseIntPipe) id: number,
    @JwtUserId() jwtUserId: number,
  ) {
    return this.collectionsService.remove(jwtUserId, id)
  }
}
